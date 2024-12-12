const d = document.getElementsByTagName("button");
const dh= document.getElementsByTagName("input");

for(let tag=0; tag<d.length; tag++)
{
    const ele = d[tag];
    ele.addEventListener("mouseenter",function(){
        ele.style.boxShadow = "10px 10px 50px green";
    })
    ele.addEventListener("mouseleave",function(){
        ele.style.boxShadow = "";
    })
}

for(let tag=0; tag<dh.length; tag++)
{
        const ele = dh[tag];
        ele.addEventListener("mouseenter",function(){
            ele.style.fontSize = "40px";
        })
        ele.addEventListener("mouseleave",function(){
            ele.style.fontSize = "";
        })
}