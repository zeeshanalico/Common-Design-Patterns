class TreeType {
    private static _instances: { [key: string]: TreeType } = {};

    // Properties of the TreeType class
    public name: string;
    public color: string;
    public texture: string;
    public height: number;

    private constructor(name: string, color: string, texture: string, height: number) {
        this.name = name;
        this.color = color;
        this.texture = texture;
        this.height = height;
    }

    // Flyweight pattern: only one instance of a given type will be created
    public static getInstance(name: string, color: string, texture: string, height: number): TreeType {
        const key = `${name}-${color}-${texture}-${height}`;
        if (!this._instances[key]) {
            this._instances[key] = new TreeType(name, color, texture, height);
        }
        return this._instances[key];
    }
}

class Tree {
    private treeType: TreeType;
    private locationX: number;
    private locationY: number;

    constructor(treeType: TreeType, locationX: number, locationY: number) {
        this.treeType = treeType;
        this.locationX = locationX;
        this.locationY = locationY;
    }

    public display(): void {
        console.log(`Tree: ${this.treeType.name}, Color: ${this.treeType.color}, ` +
            `Height: ${this.treeType.height}, Location: (${this.locationX}, ${this.locationY})`);
    }
}

// Example usage of Flyweight pattern
const forest: Tree[] = [
    new Tree(TreeType.getInstance("Oak", "Green", "Rough", 20), 5, 10),
    new Tree(TreeType.getInstance("Pine", "Dark Green", "Smooth", 30), 15, 30),
    new Tree(TreeType.getInstance("Oak", "Green", "Rough", 20), 50, 60),
    new Tree(TreeType.getInstance("Pine", "Dark Green", "Smooth", 30), 25, 80),
];

// Displaying the trees in the forest
forest.forEach(tree => tree.display());
