import './App.css';
import React, {useState} from 'react';



const App = () => {
    const [symptoms, setSymptoms] = useState("")
    const [diagnoses, setDiagnoses] = useState("")
    return (
        <div className="text-center">
            <h1 >Tool</h1>
            <p>
                Symptoms: {symptoms}
            </p>
            <textarea value = {symptoms} onChange = {event => setSymptoms(event.target.value)}/>
            <br/>
            <p>
                Diagnoses: {diagnoses}
            </p>
            <textarea value = {diagnoses} onChange = {event => setDiagnoses(event.target.value)}/>
            <br/>
            <button className="text-center">Submit</button>
        </div>
    );
    
}

export default App;
