import React, { useState } from 'react';
import axios from 'axios';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import '../styles/TimeZoneSelector.css';  // Reuse the same CSS for styling

const AddSubtractDays = () => {
    const [datetime, setDatetime] = useState('');
    const [days, setDays] = useState(0);
    const [isAdd, setIsAdd] = useState(true);  // Toggle between adding and subtracting days
    const [result, setResult] = useState(null);
    const [errorMessage, setErrorMessage] = useState('');
    const [copyMessage, setCopyMessage] = useState('');
    const [isCopied, setIsCopied] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();

        // Create the data object matching the TimeDeltaRequest schema
        const data = {
            datetime_str: datetime,
            timedelta_days: isAdd ? days : -days,
        };

        // Send a POST request to the backend with the data object
        axios.post('http://127.0.0.1:8000/user/add-subtract-timedelta', data)
            .then(response => {
                setResult(response.data);
                setErrorMessage('');  // Clear any previous error message
                setCopyMessage('');  // Clear any previous copy message
                setIsCopied(false);  // Reset the copied state
            })
            .catch(error => {
                if (error.response && error.response.data.detail) {
                    setErrorMessage(error.response.data.detail);
                } else {
                    setErrorMessage('An unexpected error occurred. Please try again.');
                }
                setResult(null);  // Clear any previous result
            });
    };

    const handleCopyToClipboard = () => {
        if (result) {
            navigator.clipboard.writeText(`Result: ${result.result}`).then(() => {
                setCopyMessage('Result copied to clipboard!');
                setIsCopied(true);
            }).catch(() => {
                setCopyMessage('Failed to copy result.');
                setIsCopied(false);
            });
        }
    };

    const toggleAddSubtract = () => {
        setIsAdd(!isAdd);
    };

    return (
        <div className="container my-4">
            <div className="row justify-content-center">
                <div className="col-md-6">
                    <div className="left-panel p-3 rounded">
                        <h2>Enter Datetime</h2>
                        <form id="main-form" onSubmit={handleSubmit}>
                            <div className="mb-3">
                                <textarea
                                    id="main-form"
                                    className="form-control datetime-input"
                                    value={datetime}
                                    onChange={(e) => setDatetime(e.target.value)}
                                    placeholder="Enter datetime in string format"
                                    required
                                />
                            </div>
                            <div className="mb-3 d-flex justify-content-center align-items-center position-relative">
                                <button
                                    type="button"
                                    className="btn btn-primary toggle-button"
                                    onClick={toggleAddSubtract}
                                >
                                    {isAdd ? '+' : '-'}
                                </button>
                                <div className="info-icon-wrapper">
                                    <InfoOutlinedIcon className="info-icon" fontSize="medium" />
                                    <span className="info-text">Click to toggle between adding or subtracting days.</span>
                                </div>
                            </div>
                            <div className="mb-3 d-flex justify-content-center">
                                <input
                                    type="number"
                                    className="form-control"
                                    value={days}
                                    onChange={(e) => setDays(e.target.value)}
                                    placeholder="Enter number of days"
                                    required
                                />
                            </div>
                            <div className="d-flex justify-content-center">
                                <button type="submit" className="btn btn-primary submit-button">Submit</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <div className="row justify-content-center">
                <div className="col-md-6">
                    {errorMessage && (
                        <div className="alert alert-danger mt-4" role="alert">
                            {errorMessage}
                        </div>
                    )}
                    {result && (
                        <div
                            className={`result-container mt-4 p-3 rounded ${isCopied ? 'copied' : ''}`}
                            onClick={handleCopyToClipboard}
                        >
                            <h2>Result:</h2>
                            <p className="result-text">Result: {result.result}</p>
                            {copyMessage && <p className="copy-message">{copyMessage}</p>}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default AddSubtractDays;
