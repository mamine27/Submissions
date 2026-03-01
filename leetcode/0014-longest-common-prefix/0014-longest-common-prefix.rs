impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut ans = String::new();
        let mut mn = 1 << 20;
        for i in 0..strs.len(){
            mn = mn.min(strs[i].len())
        }
        let chars_vecs: Vec<Vec<char>> = strs.iter()
    .map(|s| s.chars().collect())
    .collect();
        for i in 0..mn{
            let mut ch : char = chars_vecs[0][i];
            let mut ask : bool = false;
            for j in 0..strs.len(){
                if (ch != chars_vecs[j][i]){
                    ask = true;
                }
            }
            if (ask == true){
                break;
            }
            ans.push(ch);
        }

        ans
        
    }
}