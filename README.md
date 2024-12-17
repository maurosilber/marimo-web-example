# Marimo Web Example

Run app in browser going to <https://maurosilber.github.io/marimo-web-example>.

Use [data.csv](./data.csv) as an example input file.

## Develop

```
git clone https://github.com/maurosilber/marimo-web-example
pixi run <task>
```

where `<task>`:

- `edit`: opens the notebook (`app.py`) in edit mode in a browser.
- `app`: starts a server to run the notebook in app mode.
- `web-app`: starts a static web-server to run the notebook as self-contained WASM app.

The GitHub workflow <.github/workflows/deploy.yml>
builds the WASM version of the app with `pixi run build-web-app`
and publishes it to GitHub Pages (<https://maurosilber.github.io/marimo-web-example>).
