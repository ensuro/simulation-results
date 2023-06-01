"""
Utility to transform pickled results to the format used by the frontend:

  - One metadata file with the configs, dates and other details
  - One results file with just the simulation result arrays

Both files in JSON format for less coupling and better portability and safety.
"""
import argparse
import json
import pickle
import os
import os.path
import numpy as np
import datetime

parser = argparse.ArgumentParser(description="Transform pickled results to JSON")
parser.add_argument("filename", type=str, help="Filename of the pickled results")
parser.add_argument(
    "--name",
    required=True,
    type=str,
    help="Descriptive user-friendly name for this results file",
)
parser.add_argument(
    "--output-dir", type=str, default="results", help="Output directory"
)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def get_or_create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


def main(args):
    with open(args.filename, "rb") as f:
        pickle_data = pickle.load(f)

    basename = os.path.splitext(os.path.basename(args.filename))[0]

    meta = {
        "date": pickle_data["date"],
        "name": args.name,
        "configs": pickle_data["configs"],
        "results_file": os.path.join("results", f"{basename}.json"),
    }
    meta_dir = get_or_create_dir(os.path.join(args.output_dir, "meta"))
    with open(os.path.join(meta_dir, f"{basename}.json"), "w") as f:
        json.dump(meta, f, cls=CustomJSONEncoder, indent=True)

    results_dir = get_or_create_dir(os.path.join(args.output_dir, "results"))
    with open(os.path.join(results_dir, f"{basename}.json"), "w") as f:
        json.dump(pickle_data["results"], f, cls=CustomJSONEncoder, indent=True)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
