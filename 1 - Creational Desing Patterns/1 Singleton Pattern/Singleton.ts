class Singleton {

    private static _instance: null | Singleton = null;
    public value: String | null = null;

    constructor(value: String | null) {
        this.value = value;
        if (Singleton._instance != null)
            // throw (new Error("this is Singleton class"));
            return Singleton._instance;// if already instance exists then return that instance
        else
            Singleton._instance = this;

    }

    print(): void {
        console.log(this.value);
    }

}

export default new Singleton('sdf');