impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let st = x.to_string();
        let nst : String = st.chars().rev().collect();
        let bl : bool = st == nst;
        bl
        
    }
}