#!/usr/bin/node
class Rectangle{
    constructor(w, h)
    {
        if (isNaN(w)    ||isNaN(h)  ||w<=0 ||h<=0)
        {

        }
        else
        {
            this.width = w;
            this.height = h;
        }
    }
    print() {
        for (let i=0;i<this.height;i++)
        {
            console.log('X'.repeat(this.width));

        }
        
    }
    rotate(){
        let tmp = this.height;
        this.height=this.width;
        this.width=tmp;
    }
    double()
    {
        this.height=this.height*2;
        this.width=this.width*2;
    }
}
module.exports= Rectangle;