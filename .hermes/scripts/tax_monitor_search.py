# -*- coding: utf-8 -*-
import imaplib, email, json, re, os, sys
import socks, socket
from email.header import decode_header
from datetime import datetime, timedelta

CRED = r"F:\aitoptools\.hermes\secrets\gmail_credentials.json"
HERMES_ENV = os.path.join(os.environ.get("LOCALAPPDATA", r"C:\Users\Administrator\AppData\Local"), "hermes", ".env")
OUT = r"F:\aitoptools\.hermes\tmp\tax-monitor-result.json"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

d = json.load(open(CRED, encoding="utf-8"))
USER = d["user"]
try:
    _env = open(HERMES_ENV, encoding="utf-8").read()
    _m = re.search(r"^IMAP_PASSWORD=(\S+)", _env, re.M)
    PWD = _m.group(1).strip().strip('"').strip("'") if _m else d["app_password"]
except Exception:
    PWD = d["app_password"]

TAX_KEYWORDS = ["w-8", "w8", "tax", "legal", "1099", "tax document", "taxation", "withholding"]

def dec(s):
    if not s:
        return ""
    out = []
    for txt, enc in decode_header(s):
        if isinstance(txt, bytes):
            try:
                out.append(txt.decode(enc or "utf-8", errors="replace"))
            except Exception:
                out.append(txt.decode("utf-8", errors="replace"))
        else:
            out.append(txt)
    return "".join(out)

def connect():
    last_err = None
    try:
        M = imaplib.IMAP4_SSL(d["imap_host"], d["imap_port"], timeout=25)
        M.login(USER, PWD)
        return M, "direct"
    except Exception as e:
        last_err = e
    try:
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 7892)
        socket.socket = socks.socksocket
        M = imaplib.IMAP4_SSL(d["imap_host"], d["imap_port"], timeout=40)
        M.login(USER, PWD)
        return M, "socks5"
    except Exception as e2:
        raise RuntimeError("direct: %r; socks5: %r" % (last_err, e2))

def main():
    since_str = (datetime.utcnow() - timedelta(hours=26)).strftime("%d-%b-%Y")
    M, mode = connect()
    M.select("INBOX", readonly=True)
    ids_set = set()
    for dom in ["printful.com", "mail.printful.com"]:
        try:
            typ, data = M.search(None, '(FROM "%s" SINCE "%s")' % (dom, since_str))
            if data and data[0]:
                for i in data[0].split():
                    ids_set.add(i)
        except Exception as e:
            print("search err", dom, repr(e), file=sys.stderr)
    try:
        typ, data = M.search(None, '(SINCE "%s" OR SUBJECT "Tax" OR SUBJECT "tax" OR SUBJECT "W-8" OR SUBJECT "Legal")' % since_str)
        if data and data[0]:
            for i in data[0].split():
                ids_set.add(i)
    except Exception as e:
        print("search err tax kw", repr(e), file=sys.stderr)

    results = []
    for i in sorted(ids_set):
        try:
            typ, md = M.fetch(i, "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT DATE)])")
            if not md or not md[0]:
                continue
            msg = email.message_from_bytes(md[0][1])
            frm = dec(msg.get("From", ""))
            subj = dec(msg.get("Subject", ""))
            date = msg.get("Date", "")
            low_subj = subj.lower()
            low_frm = frm.lower()
            is_printful = "printful" in low_frm
            is_tax = any(k in low_subj for k in TAX_KEYWORDS)
            if is_printful or is_tax:
                results.append({"id": i.decode(), "from": frm, "subject": subj, "date": date, "is_printful_sender": is_printful, "is_tax_subject": is_tax})
        except Exception as e:
            print("fetch err", i, repr(e), file=sys.stderr)
    M.logout()

    obj = {"mode": mode, "since": since_str, "email": USER, "count": len(results), "results": results, "checked_at_utc": datetime.utcnow().isoformat() + "Z"}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    print(json.dumps(obj, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("FATAL:", repr(e), file=sys.stderr)
        sys.exit(1)
