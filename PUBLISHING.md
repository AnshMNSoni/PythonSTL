# Publishing pythonstl to PyPI

This document provides step-by-step instructions for building and publishing the pythonstl package to PyPI.

## Prerequisites

Install required tools:

```bash
pip install --upgrade pip
pip install maturin twine build
```

## Step 1: Clean Previous Builds

Remove any existing build artifacts:

```bash
# Windows PowerShell
Remove-Item -Recurse -Force dist, target, build, *.egg-info -ErrorAction SilentlyContinue

# Linux/Mac
rm -rf dist target build *.egg-info
```

## Step 2: Build the Distribution

For hybrid Python/Rust packages using Maturin:

```bash
# Build wheel and sdist with maturin
maturin build --release
```

Or using `python -m build` (which invokes maturin as the build backend defined in `pyproject.toml`):

```bash
python -m build
```

This creates distribution artifacts in `target/wheels/` or `dist/`:
- `dist/pythonstl-1.1.9.tar.gz` (source distribution)
- `dist/pythonstl-1.1.9-*.whl` (compiled wheel)

## Step 3: Validate the Build

Check the distribution files for errors:

```bash
twine check dist/*
```

Expected output:
```
Checking dist/pythonstl-0.1.0-py3-none-any.whl: PASSED
Checking dist/pythonstl-0.1.0.tar.gz: PASSED
```

## Step 4: Test on TestPyPI (Recommended)

### Upload to TestPyPI

```bash
twine upload --repository testpypi dist/*
```

You'll be prompted for credentials. Use:
- Username: `__token__`
- Password: Your TestPyPI API token (starts with `pypi-`)

### Install from TestPyPI

Test the installation:

```bash
pip install --index-url https://test.pypi.org/simple/ pythonstl
```

### Verify Installation

```python
python -c "from pythonstl import vector; v = vector(); v.push_back(1); print('✓ Installation successful')"
```

## Step 5: Publish to Production PyPI

### Using API Token (Recommended)

```bash
twine upload dist/* -u __token__ -p YOUR_PYPI_API_TOKEN
```

**Security Best Practices:**
- Never commit API tokens to version control
- Store tokens in environment variables or password managers
- Use project-scoped tokens when possible
- Rotate tokens periodically

### Using Environment Variable

Set your token as an environment variable:

```bash
# Windows PowerShell
$env:TWINE_PASSWORD = "pypi-YOUR_TOKEN_HERE"
twine upload dist/* -u __token__

# Linux/Mac
export TWINE_PASSWORD="pypi-YOUR_TOKEN_HERE"
twine upload dist/* -u __token__
```

### Using .pypirc (Alternative)

Create `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE
```

**Warning:** Ensure `.pypirc` has restricted permissions (chmod 600 on Unix).

Then upload:

```bash
twine upload dist/*
```

## Step 6: Verify Publication

After successful upload:

1. Visit https://pypi.org/project/pythonstl/
2. Install from PyPI:
   ```bash
   pip install pythonstl
   ```
3. Test the installation:
   ```python
   from pythonstl import stack, queue, vector, stl_set, stl_map, priority_queue
   print("✓ All imports successful")
   ```

## Troubleshooting

### Build Fails

- Ensure `pyproject.toml` is valid
- Check that all package directories have `__init__.py`
- Verify Python version >= 3.10

### Upload Fails

- **403 Forbidden**: Check API token permissions
- **400 Bad Request**: Package name may already exist
- **File already exists**: Version already published (increment version)

### Import Errors After Installation

- Clear pip cache: `pip cache purge`
- Reinstall: `pip uninstall pythonstl && pip install pythonstl`
- Check for naming conflicts with other packages

## Version Management

For future releases:

1. Update version in `pythonstl/__init__.py`
2. Update version in `pyproject.toml`
3. Create git tag: `git tag v0.1.1`
4. Rebuild and republish

## Security Checklist

Before publishing:

- [ ] No hardcoded secrets in code
- [ ] No sensitive data in examples
- [ ] LICENSE file included
- [ ] README.md is accurate
- [ ] All tests pass
- [ ] Version number is correct
- [ ] API token is secure

## Post-Publication

1. Create GitHub release with changelog
2. Update documentation
3. Announce on relevant channels
4. Monitor PyPI download stats
5. Respond to issues and feedback

## Resources

- PyPI: https://pypi.org/
- TestPyPI: https://test.pypi.org/
- Packaging Guide: https://packaging.python.org/
- Twine Documentation: https://twine.readthedocs.io/
