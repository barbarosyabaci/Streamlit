# Independent Streamlit Cloud deployment

Deploy `cloud_app.py` from branch `codex/ran-cloud` using Python **3.11**.
The existing production entry point is unchanged.

The cloud entry point preserves the original RAN modules, algorithms, bundled
fiber datasets, maps, images, CSV uploads and downloads. Existing demo-only
sections remain demo-only; they are not newly implemented ML models.

Configure these values in Streamlit Cloud's encrypted Secrets settings:

```toml
MONGODB_URI = "<MongoDB connection string>"
ADMIN_PASSWORD = "<a strong administration password>"
```

Never commit actual secrets. CSV processing works without MongoDB configuration.
Database administration is password protected. Toolkit accepts an uploaded
GeoJSON boundary file with a NAME_2 column rather than a Windows-only file path.
The original repository contains a hardcoded database credential; rotate it
before production use. Removing it from this entry point does not remove
it from the original files or Git history.

## Local run

```powershell
python -m pip install -r requirements.txt
python -m streamlit run cloud_app.py
```

Use Python 3.11 and keep the working directory at this repository root.
