import React from 'react'
import { Button } from 'semantic-ui-react'


export const From = ({ userInput, onChange, handleInputSubmit }) => {
    
    const handleChangeSymptoms = (event) => {
        onChange({
            symptoms: event.target.value,
            diagnoses: userInput.diagnoses
        })
    }
    const handleChangeDiagnoses = (event) => {
        onChange({
            symptoms: userInput.symptoms,
            diagnoses: event.target.value
        })
    }

    const handleSubmit = (event) => {
        event.preventDefault()
        handleInputSubmit()
    }
    return (
        <>
            <form onSubmit={handleSubmit}> 
                <input type='text' required value={userInput.symptoms} onChange={handleChangeSymptoms}></input>
                <input type='text' required value={userInput.diagnoses} onChange={handleChangeDiagnoses}></input>
                <input type='submit'></input>
            </form>

            <form onSubmit={handleSubmit}>
                <p className="text-15">
                    Symptoms: {userInput.symptoms}
                </p>
                <textarea required value = {userInput.symptoms} onChange = {handleChangeSymptoms}/>
                <p className="text-15">
                    Diagnoses: {userInput.diagnoses}
                </p>
                <textarea required value = {userInput.diagnoses} onChange = {handleChangeDiagnoses}/>
                <br/>
                <Button type="submit" content='Search' />
            </form>
        </>
    )
}