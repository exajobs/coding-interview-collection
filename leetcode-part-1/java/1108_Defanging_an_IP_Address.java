class Solution {
    public String defangIPaddr(String address) {
        // replace
        return address.replace(".", "[.]");
    }
    /* public String defangIPaddr(String address) {
        // split and join
        return String.join("[.]", address.split("\\."));
    } */
    /* public String defangIPaddr(String address) {
        // replace
        return address.replaceAll("\\.", "[.]");
    } */
    /* public String defangIPaddr(String address) {
        // new string
        StringBuilder sb = new StringBuilder();
        for (char c : address.toCharArray()) {
            sb.append(c == '.' ? "[.]" : c);
        }
        return sb.toString();
    } */
}
