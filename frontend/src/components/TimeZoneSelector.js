import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/TimeZoneSelector.css';  // Custom CSS

const TimeZoneSelector = () => {
    const [timezones, setTimezones] = useState([]);
    const [selectedTimezone, setSelectedTimezone] = useState('America/New_York');  // Default to "America/New_York"
    const [datetime, setDatetime] = useState('');
    const [result, setResult] = useState(null);
    const [errorMessage, setErrorMessage] = useState('');  // Track error messages from the API
    const [copyMessage, setCopyMessage] = useState('');
    const [isCopied, setIsCopied] = useState(false);  // Track if result is copied

    useEffect(() => {
        // Fetch the timezones from the backend
        axios.get('http://127.0.0.1:8000/user/timezones/')
            .then(response => {
                setTimezones(response.data.timezones);  // Store the full timezone format
            })
            .catch(error => console.error('Error fetching timezones:', error));
    }, []);

    const handleSubmit = (e) => {
        e.preventDefault();

        // Create the data object matching the TimeDiffRequest schema
        const data = {
            datetime_str: datetime,
            timezone: selectedTimezone,
        };

        // Send a POST request to the backend with the data object
        axios.post('http://127.0.0.1:8000/user/get-difference', data)
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
            const textToCopy = `Calculated From: ${result.calculated_from}\nTime Difference: ${result.result}`;
            navigator.clipboard.writeText(textToCopy).then(() => {
                setCopyMessage('Result copied to clipboard!');
                setIsCopied(true);
            }).catch(() => {
                setCopyMessage('Failed to copy result.');
                setIsCopied(false);
            });
        }
    };

    return (
        <div className="container my-4">
            <div className="row">
                <div className="col-md-4">
                    <div className="left-panel p-3 rounded">
                        <h2>Select Timezone</h2>
                        {timezones.map((tz) => (
                            <div key={tz} className="form-check">
                                <label className="form-check-label timezone-label" htmlFor={tz}>
                                    <input
                                        type="radio"
                                        className="form-check-input"
                                        id={tz}
                                        name="timezone"
                                        value={tz}
                                        checked={selectedTimezone === tz}
                                        onChange={(e) => setSelectedTimezone(e.target.value)}
                                    />
                                    {tz.split('/').pop().replace('_', ' ')}  {/* Display only the city name */}
                                </label>
                            </div>
                        ))}
                    </div>
                </div>
                <div className="col-md-8">
                    <div className="right-panel p-3 rounded">
                        <h2>Enter Datetime</h2> {/* Match heading style */}
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
                            <button type="submit" className="btn btn-primary">Submit</button>
                        </form>
                    </div>
                </div>
            </div>
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
                    <h2>Result:</h2> {/* Match heading color */}
                    {result.future_warning && <p className="warning-text">Warning: The input datetime is in the future!
                        Thus, we calculated everything <b>from</b> your date.</p>}
                    <p className="result-text">Calculated with: {result.calculated_from}</p>
                    <p className="result-text">Time Difference: {result.result}</p>
                    {copyMessage && <p className="copy-message">{copyMessage}</p>}
                </div>
            )}
        </div>
    );
};

export default TimeZoneSelector;
