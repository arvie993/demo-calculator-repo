# Spanish README Translation GitHub Action

This GitHub Action automatically translates the repository's README.md file to Spanish whenever changes are made.

## How it works

1. **Trigger**: The workflow triggers on:
   - Push to main/master branches when README.md is modified
   - Pull requests to main/master branches when README.md is modified

2. **Translation Process**:
   - Uses a Python script that creates a comprehensive Spanish translation
   - Includes timestamps to track when the translation was last updated
   - Maintains proper markdown formatting and code block preservation

3. **Output**: Creates/updates `README_es.md` with the Spanish translation

## Files

- `.github/workflows/translate-readme.yml` - GitHub Action workflow definition
- `.github/scripts/translate_readme.py` - Translation script
- `README_es.md` - Generated Spanish README

## Manual Usage

You can run the translation script manually:

```bash
python .github/scripts/translate_readme.py
```

## Notes

- Uses static translation content optimized for this calculator project
- Automatically commits changes back to the repository
- Includes proper git configuration for the GitHub Action bot
- No external API dependencies required