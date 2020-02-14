

/////////  PROMPT #130  //////////////
// Given an array of points that represent the 3 vertices of a triangle,
// and a point K, return true if K is inside the triangle.
////////////////////////////////////


/*

c1 = dotProd(A,P)
c2 = dotProd(B,P)
c3 = dotProd(C,P)

if you do know nothing about the given order of vertices V1, V2, V3, then P is inside the triangle if
(c1> 0 && c2> 0 && c3 > 0) || (c1< 0 && c2< 0 && c3 < 0).
*/

const dotProd = (V1, V2) => {
    //.log(V1,V2);
    return (V1[0]*V2[1]) - (V1[1]*V2[0])

}


const isInTriangle = (triangle, P) => {
  var [A,B,C] = triangle;
  //console.log(A,B,C,P);
  var c1 = dotProd( [A[0]-B[0],A[1]-B[1]], [A[0]-P[0],A[1]-P[1]] ); // (A-B), (A-P)
  var c2 = dotProd( [B[0]-C[0],B[1]-C[1]], [B[0]-P[0],B[1]-P[1]] ); // (B-C), (B-P)
  var c3 = dotProd( [C[0]-A[0],C[1]-A[1]], [C[0]-P[0],C[1]-P[1]] ); // (C-A), (C-P)
  //console.log(c1,c2,c3);
  if (c1 >=0 && c2>=0 && c3 >=0){
    return true;
  }
  else if (c1 <=0 && c2 <= 0 && c3 <=0){
    return true;
  }
  else{
    return false;
  }
}


let triangle = [ [0,0], [0,3], [4,0] ]
console.log(isInTriangle(triangle, [2,1]));//TRUE

console.log(isInTriangle(triangle, [3,2]));//FALSE


/* TESTS

let triangle = [ [0,0], [0,3], [4,0] ]

isInTriangle(triangle, [2,1])
> true

isInTriangle(triangle, [3,2])
> false

*/
