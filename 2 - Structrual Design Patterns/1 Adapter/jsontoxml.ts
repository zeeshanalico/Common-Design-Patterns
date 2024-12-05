interface XmlDataProcessor {
    processXmlData(xmlData: string): void;
}

class JsonDataService {
    getJsonData(): Record<string, any> {
        return {
            name: "John Doe",
            age: 30,
            city: "New York"
        };
    }
}

class JsonToXmlAdapter implements XmlDataProcessor {
    private jsonDataService: JsonDataService;

    constructor(jsonDataService: JsonDataService) {
        this.jsonDataService = jsonDataService;
    }

    processXmlData(): void {
        // Convert JSON to XML
        const jsonData = this.jsonDataService.getJsonData();
        const xmlData = this.convertJsonToXml(jsonData);
        console.log(`Converted XML data:\n${xmlData}`);
    }

    private convertJsonToXml(jsonData: Record<string, any>): string {
        let xmlData = "<root>\n";
        for (const key in jsonData) {
            xmlData += `  <${key}>${jsonData[key]}</${key}>\n`;
        }
        xmlData += "</root>";
        return xmlData;
    }
}

// 5. Client code
const jsonService = new JsonDataService();
const jsonToXmlAdapter = new JsonToXmlAdapter(jsonService);

jsonToXmlAdapter.processXmlData();  // Outputs the JSON data in XML format
