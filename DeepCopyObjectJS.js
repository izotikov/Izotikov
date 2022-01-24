let user = { //Making a deep object
    name: "Иван",
    sizes: {
        height: 182,
        width: 50,
        wines: {
            cool: 1,
            array : ["a", 'b', 2]
        }
    }
};

function cloneObj(obj) {
    let newObj = {};
    for (let key in obj) {
        if (typeof(obj[key]) === "object") { //Recursion
            newObj[key] = cloneObj(obj[key]);
        } else {
            newObj[key] = obj[key]; //Copy simple keys.
        }
    }
    return newObj;
}

let a = cloneObj(user); //Some tests to change different values.
user.sizes.height++;
user.sizes.wines.cool += 10;
a.sizes.width = "Prestige";
user.sizes.wines.array[1] = 'AAAd';
a.sizes.wines.array[1] = '14';
console.log(a);
console.log(user);

