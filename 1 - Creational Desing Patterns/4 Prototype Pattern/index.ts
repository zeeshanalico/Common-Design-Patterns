interface Prototype {
    clone(): Prototype;
}

abstract class Vehicle implements Prototype {
    model: string;
    engine: string;
    brand: string;

    constructor(vehicle: Vehicle) { // Copy constructor
        this.model = vehicle.model;
        this.engine = vehicle.engine;
        this.brand = vehicle.brand;
    }
    abstract clone(): Vehicle;
}

class Car extends Vehicle {
    toSpeed: number;

    constructor(bus: { model: string; engine: string; brand: string; toSpeed: number });
    constructor(car: Car) {
        super(car); // Calls Vehicle's copy constructor
        this.toSpeed = car.toSpeed;
    }

    clone(): Car {
        return new Car(this);
    }
}

class Bus extends Vehicle {
    wheels: number;

    //TypeScript: Multiple signatures with a single function or constructor implementation. 
    //Java/C++: Multiple distinct implementations, each with its own parameter list (signature).This is true overloading:
    //constructor overloading
    constructor(bus: { model: string; engine: string; brand: string; wheels: number });
    constructor(bus: Bus) {
        super(bus); // Calls Vehicle's copy constructor//polymorphism
        this.wheels = bus.wheels;
    }

    clone(): Bus {
        return new Bus(this);
    }
}

const originalBus = new Bus({ model: "City Bus", engine: "Diesel", brand: "Volvo", wheels: 6 ,} );
const clonedBus = originalBus.clone();
const originalCar = new Car({ model: "City Bus", engine: "Diesel", brand: "Volvo", toSpeed: 6 ,} );

console.log("Original Bus:", originalBus);
console.log("Cloned Bus:", clonedBus);
