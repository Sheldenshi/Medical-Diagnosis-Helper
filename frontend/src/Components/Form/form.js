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
                <p className="text-15">
                    Symptoms: 
                </p>
                <textarea required value = {userInput.symptoms} onChange = {handleChangeSymptoms}/>
                <p className="text-15">
                    Diagnoses:
                </p>
                <textarea required value = {userInput.diagnoses} onChange = {handleChangeDiagnoses}/>
                <br/>
                <Button type="submit" content='Search' />
            </form>
        </>
    )
}