import os
import json

try:
    import pikepdf
except Exception:
    pikepdf = None


def check_pdf_structure(path: str):
    res = {
        "path": path,
        "exists": False,
        "header_ok": False,
        "header_version": None,
        "eof_ok": False,
        "eof_offset": None,
    }

    if not os.path.isfile(path):
        return res
    res["exists"] = True
    with open(path, "rb") as f:
        data = f.read()

    if data.startswith(b"%PDF-"):
        res["header_ok"] = True
        try:
            ver = data[5:8].decode("ascii", errors="ignore")
            res["header_version"] = ver
        except Exception:
            res["header_version"] = None

    idx = data.rfind(b"%%EOF")
    if idx != -1:
        res["eof_ok"] = True
        res["eof_offset"] = idx
    else:
        res["eof_ok"] = False
    return res


def can_open_with_pikepdf(path: str):
    if pikepdf is None:
        return {"available": False, "can_open": False, "error": "pikepdf not installed"}
    try:
        with pikepdf.Pdf.open(path):
            return {"available": True, "can_open": True, "error": None}
    except Exception as e:
        return {"available": True, "can_open": False, "error": str(e)}


def try_repair_with_pikepdf(path: str, out_path: str):
    """Attempt to load and save via pikepdf which can fix some structural issues."""
    if pikepdf is None:
        return {"success": False, "error": "pikepdf not installed"}
    try:
        pdf = pikepdf.Pdf.open(path)
        pdf.save(out_path)
        return {"success": True, "out_path": out_path}
    except Exception as e:
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("file")
    args = p.parse_args()
    s = check_pdf_structure(args.file)
    s.update(can_open_with_pikepdf(args.file))
    print(json.dumps(s, indent=2))
