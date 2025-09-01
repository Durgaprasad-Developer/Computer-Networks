import java.util.ArrayList;

public class GFGweighted {
    static class Pair{
        int node, weight;
        Pair(int node, int weight){
            this.node = node;
            this.weight = weight;
        }
    }

    public static void main(String[] args){
        int n = 3;

        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();

        for(int i=0;i<=n;i++){
            adj.add(new ArrayList<Pair>());
        }

        addEdge(adj, 1, 2, 4);
        addEdge(adj, 2,3,5);
        addEdge(adj, 1, 3, 10);

        for(int i=1; i<=n; i++){
            System.out.print(i + " -> ");
            for(Pair p : adj.get(i)){
                System.out.print("(" + p.node + ", "+ p.weight + " )");
            }
            System.out.println();
        }
    }

    static void addEdge(ArrayList<ArrayList<Pair>> adj, int v, int u, int w){
        adj.get(v).add(new Pair(u, w));
        adj.get(u).add(new Pair(v,w)); // remove this line for directed graph
    }
}
