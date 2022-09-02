class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> inStack = new Stack<>();
        int posPush = 0, posPop = 0;
        while (posPush != pushed.length) {
            int curr = pushed[posPush];
            while (!inStack.empty() && popped.length > 0 && inStack.peek() == popped[posPop]) {
                inStack.pop();
                posPop++;
            }
            if (popped.length == 0) break;
            if (curr == popped[posPop]) posPop++;
            else inStack.push(curr);
            posPush++;
        }
        while (!inStack.empty() && popped.length > 0 && inStack.peek() == popped[posPop]) {
            inStack.pop();
            posPop++;
        }
        if (inStack.empty()) return true;
        return false;
    }
}
