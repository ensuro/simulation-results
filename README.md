# Simulations

The `meta` directory holds the metadata for the available results.

Each metadata file points to a file in `results` that has the actual results.

All files are JSON for better portability and less coupling with the simulator component.

The pickled results from the simulator can be converted to JSON with the script `pickle2json.py`.

The results and metadata use the same structure as the ones created by the [ens-simulator](https://github.com/ensuro/ens-simulator) tool.

Once the results are here they can be visualized in the `simulator-frontend`
