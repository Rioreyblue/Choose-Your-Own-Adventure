import { useState, useEffect } from "react";
import {useParams, useNavigate} from "react-router-dom"
import axios from 'axios';
import LoadingStatus from "./LoadingStatus.jsx"
import StoryGame from "./StoryGame";

const API_BASE_URL = "/api"

function StoryLoader(){
    const {id} = useParams();
    const navigate = useNavigate();
    const [story, setStory] =   useState(null);
    const [loading, setLoading] = useState(null);
    const [error, setError] = useState(null)

    useEffect(() => {
        loadStory(id)
    }, [id])


    const loadStory = async (storyId) => {
        setLoading(true)
        setError(null)

        try{
            const response = await axios.get(`${API_BASE_URL}/stories/${storyId}/complete`)
            setStory(response.data)
            setLoading(false)
        } catch (err){
            if (err.response?.status === 404) {
                setError("Story not found.")
            } else {
                setError("Faild to load story")
            }
        } finally{
            setLoading(false)
        }
    }

    const createNewStory = () => {
        navigate("/")
    }

     if (loading){
        return <LoadingStatus theme={"story"}/>
     }

     if (error){
        return <div className="story-loader">
            <div className="error-message">
                <h2>Story not Found</h2>
                <p>{error}</p>
                <button onClick={createNewStory}>Go to Story Generator</button>
            </div>
        </div>
     }
        //navigate to thata page
     if (story){
        return <div className="story-loader">
            <StoryGame story={story} onNewStory={createNewStory}/>
        </div>
     }
}

export default StoryLoader;