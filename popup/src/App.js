import React, {useState} from 'react';
import { Dimmer, Loader, Image, Segment } from 'semantic-ui-react'

import { From } from './Components/Form/form'
import { ListResult } from './Components/SearchResult/showResult'

const App = () => {
    const [input, setInput] = useState({
        symptoms: "",
        diagnoses: ""
    })
    const [result, setResult] = useState([])
    const [searching, setSearching] = useState(false)
    
    const handleChange = (inputValue) => {
        setInput(inputValue)
    }
    const handleResult = (resultJson) => {
        const resultList = []
        for (var i = 0; i < Object.keys(resultJson).length; i++) {
            resultList.push(resultJson[i])
        }
        //console.log(resultList);
        setResult(resultList)
    }
    const handleInputSubmit = () => {
        setSearching(true)
        fetch('/api/search', {
            method: 'POST',
            body: JSON.stringify({
                symptoms: input.symptoms,
                diagnoses: input.diagnoses
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        }).then(response => response.json())
        .then(resultJson => {
            //(resultJson)
            setInput({
                symptoms: "",
                diagnoses: ""
            })
            setSearching(false)
            handleResult(resultJson)
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
