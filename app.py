import marimo

__generated_with = "0.10.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import altair
    import io
    return altair, io, mo, pd


@app.cell
def _(mo):
    file = mo.ui.file().form()

    mo.hstack([mo.md("Upload a CSV file:"), file], justify="center", wrap=True)
    return (file,)


@app.cell
def _(file, io, pd):
    df = pd.read_csv(io.BytesIO(file.value[0].contents))
    return (df,)


@app.cell
def _(df, mo):
    x = mo.ui.dropdown(df.columns, value=df.columns[0])
    y = mo.ui.dropdown(df.columns, value=df.columns[1])
    dropdowns = mo.hstack(["x =", x, "y =", y], justify="center")
    return dropdowns, x, y


@app.cell
def _(altair, df, dropdowns, mo, x, y):
    chart = altair.Chart(df).mark_point().encode(x=x.value, y=y.value)
    chart = mo.vstack([dropdowns, mo.ui.altair_chart(chart)])
    return (chart,)


@app.cell
def _(chart, df, mo):
    mo.hstack([chart, df], widths=[1, 1])
    return


if __name__ == "__main__":
    app.run()
