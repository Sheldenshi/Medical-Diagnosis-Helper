
import React, {useState} from 'react';



const App = () => {
    const [symptoms, setSymptoms] = useState("")
    const [diagnoses, setDiagnoses] = useState("")
    return (
        <div className="text-center">
            <h1>Medical Resources Search Helper</h1>
            <p className="text-20">
                Symptoms: {symptoms}
            </p>
            <textarea value = {symptoms} onChange = {event => setSymptoms(event.target.value)}/>
            <p className="text-20">
                Diagnoses: {diagnoses}
            </p>
            <textarea value = {diagnoses} onChange = {event => setDiagnoses(event.target.value)}/>
            <br/>
            <button className="text-15">Search</button>
        </div>
    );
    
}

export default App;
