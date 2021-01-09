import React, {useState, useEffect} from 'react';

import { From } from './Components/Form/form'



const App = () => {
    const [input, setInput] = useState({
        symptoms: '',
        diagnoses: ''
    })
    const [result, setResult] = useState([])

    useEffect(() => {
        fetch('/api').then(response => {
            if(response.ok) {
                return response.json()
            }
        }).then(data => setResult(data))
        }, [])

    const handleChange = (inputValue) => {
        setInput(inputValue)
    }
    const handleInputSubmit = () => {
        fetch('/api/input', {
            method: 'POST',
            body: JSON.stringify({
                symptoms: input.symptoms,
                diagnoses: input.diagnoses
            })
        })
    }

    return (
        <div className="text-center">
            <h1>Medical Resources Search Helper</h1>
            <From userInput={input} onChange={handleChange}/>
            {result.map(result => {
                return(
                    <ul key={result.id}>
                        <li>{result.symptoms}</li>
                        <li>{result.diagnoses}</li>
                    </ul>
                )
            })}
        </div>
    )
    
}

export default App;
