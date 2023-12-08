use h3o::{LatLng, Resolution};
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;

fn _geo_to_h3(lat: f64, lng: f64, resolution: Resolution) -> u64 {
    let coord = LatLng::new(lat, lng).expect("invalid coord");
    coord
        .to_cell(resolution)
        .try_into()
        .expect("cannot convert to str")
}

#[polars_expr(output_type=UInt64)]
pub fn geo_to_h3(inputs: &[Series]) -> PolarsResult<Series> {
    let resolution: u8 = 3;
    let ca_lat = inputs[0].f64()?;
    let ca_lng = inputs[1].f64()?;
    let out: UInt64Chunked = arity::binary_elementwise_values(ca_lat, ca_lng, |a, b| {
        _geo_to_h3(a, b, resolution.try_into().expect("hoge"))
    });
    Ok(out.into_series())
}
