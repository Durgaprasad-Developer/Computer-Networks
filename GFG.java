import java.util.*;
class GFG{
    public static void main(String[] args){
        int n = 3, m = 3;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();

        for(int i=0;i<=n;i++){
            adj.add(new ArrayList<Integer>());
        }

        addEdge(adj, 1, 2);
        addEdge(adj, 2, 3);
        addEdge(adj, 1, 3);

        for(int i=1;i<=n;i++){
            System.out.print(i + " -> ");
            for(int v : adj.get(i)){
                System.out.print(v + " ");
            }
            System.out.println();
        }
    }
    static void addEdge(ArrayList<ArrayList<Integer>> adj, int v, int u){
        adj.get(v).add(u);
        adj.get(u).add(v); //for directed graph just remove this line
    }
}