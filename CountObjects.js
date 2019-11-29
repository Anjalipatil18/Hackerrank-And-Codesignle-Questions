function getCount(objects) {
    let n=0;
    for (let i=0; i<objects.length; i++){
        if (objects[i].x==objects[i].y){
            n++;
        }
    }return n;
}
