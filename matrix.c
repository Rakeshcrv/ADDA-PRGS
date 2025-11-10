#include<stdio.h>
#define MAX_VERTICES 100
void IM(int matrix[MAX_VERTICES][MAX_VERTICES],int vertices){
    for(int i=0;i<vertices;i++){
        for(int j=0;j<vertices;j++){
            matrix[i][j]=0;
        }
    }
}
void DM(int matrix[MAX_VERTICES][MAX_VERTICES],int vertices){
    printf("Adjucency matrix:\n");
    for(int i=0;i<vertices;i++){
        for(int j=0;j<vertices;j++){
            printf("%d",matrix[i][j]);
        }printf("\n");
    }
}
int main(){
    int vertices=4;
    int edges=3;
    int edgelist[3][2]={{0,1},{1,2},{2,3}};
    int adjmatrix[MAX_VERTICES][MAX_VERTICES];
    IM(adjmatrix,vertices);
    for(int i=0;i<edges;i++){
        int u=edgelist[i][0];
        int v=edgelist[i][1];
        adjmatrix[u][v]=1;
        adjmatrix[v][u]=1;
    }
    DM(adjmatrix,vertices);
    return 0;
}