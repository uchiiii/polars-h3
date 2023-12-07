import polars as pl
from polars.type_aliases import IntoExpr
from polars.utils.udfs import _get_shared_lib_location

# Boilerplate needed to inform Polars of the location of binary wheel.
lib = _get_shared_lib_location(__file__)

@pl.api.register_expr_namespace("h3")
class H3:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def geo_to_h3(self, other: IntoExpr) -> pl.Expr:
        return self._expr._register_plugin(
            lib=lib,
            args=[other],
            symbol="geo_to_h3",
            is_elementwise=True,
        )
