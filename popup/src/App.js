import React, {useState, useEffect} from 'react';
import { Dimmer, Loader, Image, Segment } from 'semantic-ui-react'

import { From } from './Components/Form/form'
import { ListResult } from './Components/SearchResult/searchResult'

const App = () => {
    const [input, setInput] = useState({
        symptoms: "",
        diagnoses: ""
    })
    const [result, setResult] = useState([])
    const [searching, setSearching] = useState(false)
    const getResult = () => {
        fetch('/api').then(response => {
            if(response.ok) {
                return response.json()
            }
        }).then(data => setResult(data))
    }
    
    const handleChange = (inputValue) => {
        setInput(inputValue)
    }
    const handleInputSubmit = () => {
        setSearching(true)
        fetch('/api/input', {
            method: 'POST',
            body: JSON.stringify({
                symptoms: input.symptoms,
                diagnoses: input.diagnoses
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        }).then(response => response.json())
        .then(message => {
            console.log(message)
            setInput({
                symptoms: "",
                diagnoses: ""
            })
            setSearching(false)
            getResult()
        })
    }
    if (searching) {
        return (
            <div className="text-center">
                <h1>Medical Resources Search Helper</h1>
                <Segment>
                <Dimmer active>
                    <Loader size='large'>Searching</Loader>
                </Dimmer>
                <Image src='https://react.semantic-ui.com/images/wireframe/paragraph.png' />
                </Segment>
            </div>
        )
    } 
    return (
        <div className="text-center">
            <h1>Medical Resources Search Helper</h1>
            <From userInput={input} onChange={handleChange} handleInputSubmit={handleInputSubmit}/>
            <ListResult result={result}/>
            
        </div>
    )
    
}

export default App;
