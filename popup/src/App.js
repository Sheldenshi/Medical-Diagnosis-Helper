import React, {useState, useEffect} from 'react';
import { Button } from 'semantic-ui-react'



const App = () => {
    const [symptoms, setSymptoms] = useState("")
    const [diagnoses, setDiagnoses] = useState("")
    const [currentTime, setCurrentTIme] = useState(0)

    useEffect(
        () => {
        fetch('/time').then(res => res.json()).then(data => {
            setCurrentTIme(data.time)
        })
        }, []
    )
    return (
        <div className="text-center">
            <h1>Medical Resources Search Helper</h1>
            <form>
                <p className="text-15">
                    Symptoms: {symptoms}
                </p>
                <textarea value = {symptoms} onChange = {event => setSymptoms(event.target.value)}/>
                <p className="text-15">
                    Diagnoses: {diagnoses}
                </p>
                <textarea value = {diagnoses} onChange = {event => setDiagnoses(event.target.value)}/>
                <br/>
                <Button onClick={() => console.log("nothing")} content='Search' />
            </form>
            
            <p>The current time is {currentTime}.</p>
        </div>
    );
    
}

export default App;
