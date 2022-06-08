import java.util.*;

class FordFulkerson{
    public static boolean bfs(int[][] rGraph,int s,int t,int[] parent){
        boolean[] vis = new boolean[rGraph.length];
        Queue<Integer> q = new ArrayDeque<Integer>();
        q.add(s);
        vis[s] = true;
        parent[s] = -1;
        while(!q.isEmpty()){
            int it = q.poll();
            for(int i=0;i<rGraph.length;i++){
                if(vis[i] == false && rGraph[it][i] > 0){
                    if(i == t){
                        parent[i] = it;
                        return true;
                    }
                    q.add(i);
                    parent[i] = it;
                    vis[i] = true;
                }
            }
        }
        return false;
    }
    public static int FordFulkerson(int[][] graph,int s,int t){
        int maxflow = 0;
        int u,v;
        int rGraph[][] = new int[graph.length][graph[0].length];
        for(int i=0;i<graph.length;i++){
            for(int j=0;j<graph[0].length;j++){
                rGraph[i][j] = graph[i][j];
            }
        }

        int[] parent = new int[graph.length];
        
        while(bfs(rGraph,s,t,parent)){
            int path_flow = Integer.MAX_VALUE;

            for(int i=0;i<parent.length;i++){
                System.out.print(parent[i]+" ");
            }
            System.out.println();
            for (v = t; v != s; v = parent[v]) {
				u = parent[v];
				path_flow
					= Math.min(path_flow, rGraph[u][v]);
			}
            for (v = t; v != s; v = parent[v]) {
				u = parent[v];
				rGraph[u][v] -= path_flow;
				rGraph[v][u] += path_flow;
			}
            maxflow += path_flow;
        }
        for(int i=0;i<rGraph.length;i++){
            for(int j=0;j<rGraph.length;j++){
                System.out.print(rGraph[i][j]+" ");
            }
            System.out.println("");
        }

		
		return maxflow;


    }
    public static void main(String args[]){
        int graph[][] = new int[][] {
			{ 0, 22, 0, 4, 0, 0 }, 
            { 0, 0, 20, 7, 0, 0 },
			{ 0, 0, 0, 0, 0, 15 },
            { 0, 0, 0, 0, 18, 0 },
			{ 0, 0, 13, 0, 0, 20 }, 
            { 0, 0, 0, 0, 0, 0 }
		};
        System.out.println("The maxflow of the graph is:"+FordFulkerson(graph,0,5));
        
    }
}