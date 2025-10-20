# Model files and storage

This repository previously contained large model binaries which were removed from Git history to keep the repository small and healthy.

Recommended workflow

- Use Git LFS to store model binaries if you want them versioned alongside the repo.
  - Install: https://git-lfs.github.com/
  - Initialize: git lfs install
  - Track files: git lfs track "backend/src/ai_refactor/Llama-2-7B-Chat-GGML/*.bin"
  - Commit the .gitattributes that contains LFS patterns.

- Alternatively, store model weights in external storage (S3, GCS, artifact registry) and add a small downloader script in `backend/scripts/` to fetch and place the files locally when required.

Where to place model files locally

- Put the model files under `backend/src/ai_refactor/Llama-2-7B-Chat-GGML/` but do not commit them with regular git (use LFS or external storage).

If you want, I can:
- Convert the model files to Git LFS and rewrite history to re-add them as LFS objects.
- Add a small downloader script to fetch models from an external source.
