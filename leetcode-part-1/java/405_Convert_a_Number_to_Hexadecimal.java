import com.sun.corba.se.spi.orbutil.fsm.Guard.Result;

class Solution {
    public String toHex(int num) {
        String hex_map = "0123456789abcdef";
        if (num == 0) return "0";
        String res = "";
        // To avoid infinite loop caused by negative num
        while (num != 0 && res.length() < 8) {
            res = hex_map.charAt(num & 15) + res;
            num = num >> 4;
        }
        return res;
    }

    /* public String toHex(int num) {
        String hex = Integer.toHexString(num);
        return hex;
    } */
}
