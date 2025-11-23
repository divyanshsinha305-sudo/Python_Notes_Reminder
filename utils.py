import csv

def search_notes(notes, keyword):
    keyword = keyword.lower()
    results = []
    for n in notes:
        if (keyword in n["title"].lower() or
            keyword in n["body"].lower() or
            keyword in " ".join(n["tags"]).lower()):
            results.append(n)
    return results

def export_notes_csv(notes, path="notes_export.csv"):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "body", "tags", "created_at"])

        for n in notes:
            writer.writerow([n["id"], n["title"],
                            n["body"], ",".join(n["tags"]),
                            n["created_at"]])
    return path
