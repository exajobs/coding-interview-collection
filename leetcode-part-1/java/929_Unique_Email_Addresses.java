import java.util.HashSet;

class Solution {
    public int numUniqueEmails(String[] emails) {
        HashSet<String> emailSet = new HashSet<>();
        for (String email: emails) {
            String firstSplit[] = email.split("@");
            String secondSplit[] = firstSplit[0].replaceAll(".", "").split("[+]");
            emailSet.add(secondSplit[0] + firstSplit[1]);
        }     
        return emailSet.size();
    }
}
