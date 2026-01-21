import os
import json
from lxml import etree


# CHECK IF XML IS FORMED AND REPAIR IF NOT
def check_xml_wellformed(path: str):
    res = {"path": path, "exists": False, "well_formed": False, "errors": []}
    if not os.path.isfile(path):
        return res
    res["exists"] = True
    try:
        parser = etree.XMLParser(recover=False)
        etree.parse(path, parser)
        res["well_formed"] = True
        return res
    except etree.XMLSyntaxError as e:
        res["well_formed"] = False
        ## TRY TO RECOVER
        rec_parser = etree.XMLParser(recover=True)
        try:
            doc = etree.parse(path, rec_parser)
            ## COLLECT ERRORS
            for entry in rec_parser.error_log:
                res["errors"].append(str(entry))
            res["recovered"] = True
        except Exception:
            ## MARK AS NOT RECOVERED
            for entry in e.error_log:
                res["errors"].append(str(entry))
            res["recovered"] = False
        return res


# ATTEMPT TO REPAIR XML
def try_repair_xml(path: str, out_path: str):
    """Attempt to recover and write a repaired XML using lxml's recover mode."""
    try:
        parser = etree.XMLParser(recover=True)
        tree = etree.parse(path, parser)
        tree.write(out_path, encoding="utf-8", xml_declaration=True)
        return {
            "success": True,
            "out_path": out_path,
            "errors": [str(e) for e in parser.error_log],
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("file")
    args = p.parse_args()
    print(json.dumps(check_xml_wellformed(args.file), indent=2))
