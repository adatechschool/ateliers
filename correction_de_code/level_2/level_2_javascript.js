class Dinglemouse {

    constructor() {
        this.name = this.age = this.sex = 0
    }

    setAge(age) {
        this.age = age
        return this
    }

    setSex(sex) {
        this.sex = sex
        return this
    }

    setName(name) {
        this.name = name
        return this
    }

    hello() {
        return `Hello. My name is ${this.name}. I am ${this.age}. I am ${this.sex == 'M' ? "male" : "female"}.`
    }

}
