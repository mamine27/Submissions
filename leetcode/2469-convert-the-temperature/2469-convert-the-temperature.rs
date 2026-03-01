impl Solution {
    pub fn convert_temperature(celsius: f64) -> Vec<f64> {
        let kl : f64 = celsius + 273.15_f64 ;
        let fr : f64 = (celsius * 1.80) + 32.00 ;

        vec![kl,fr]
    }
}