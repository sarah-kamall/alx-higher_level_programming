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
}
module.exports= Rectangle;