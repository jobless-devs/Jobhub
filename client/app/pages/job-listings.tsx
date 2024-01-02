'use client'

import Link from 'next/link';
import React, { useEffect, useState, useRef} from 'react';
import axios from 'axios'; 

// Define Type for Job Card
type Job = {
  id: number;
  date: string;
  position: string;
  company: string;
  location: string;
  link: string;
};

type JobListingsProps = {
  jobs?: Job[]; // jobs is now an optional prop
  onBack: () => void;
};

const JobListings = ({ jobs: propJobs, onBack }: JobListingsProps) => {
  const [jobs, setJobs] = useState<Job[]>(propJobs || []);

  useEffect(() => {
    // Fetch jobs only if propJobs is not provided
    if (!propJobs) {
      const fetchJobs = async () => {
        try {
          const response = await axios.get('https://9loe6yy9pk.execute-api.us-east-1.amazonaws.com/prod/jobs');
          // Assuming response.data directly returns the array of jobs
          if (response.status === 200 && Array.isArray(response.data)) {
            setJobs(response.data);
          } else {
            console.error("API response data is not an array.");
          }
        } catch (error) {
          console.error('Error fetching jobs:', error);
        }
      };

      fetchJobs();
    }
  }, [propJobs]);

  const [visibleJobsCount, setVisibleJobsCount] = useState(10); // Start with 10 jobs

  const loadMoreJobs = () => {
    setVisibleJobsCount(currentCount => currentCount + 10); // Load 10 more jobs
  };

  const jobsToShow = jobs.slice(0, visibleJobsCount); // Show only a subset of jobs
  
  const audioRef = useRef<HTMLAudioElement>(null);  // Create a reference to the audio element

  const playAudioThenNavigate = (url : any, event : any) => {
    event.preventDefault(); // Prevent default link navigation
    const audio = audioRef.current;
    if (audio) {
      audio.play().catch(error => {
        console.error("Audio playback failed:", error);
      });
    }

    window.open(url, '_blank'); // Open in a new tab immediately
  };

  const formatDate = (dateString: string) => {
    const parts = dateString.split('-'); // Split the date string into [year, month, day]
  // Note that months are 0-indexed in JavaScript Date, so subtract 1
    const date = new Date(parseInt(parts[0]), parseInt(parts[1]) - 1, parseInt(parts[2]));
    console.log(dateString)
    const year = date.getFullYear();
    const month = date.toLocaleString('en-US', { month: 'short' }).toUpperCase(); // 'short' gives abbreviated month
    const day = date.getDate();
  
    return `${year} ${month} ${day}`;
  };


  return (
    <div className="container mx-auto">
      <button onClick={onBack} className="bg-custom-black hover:bg-custom-orange text-center text-white p-2 rounded mt-3 justify-center mx-auto">
      &#5176; Back
      </button> 
      <div className="text-center text-3xl font-bold my-4">
        <span className="text-custom-black">Job </span>
        <span className="text-custom-orange">Listings</span>
      </div>
      <div className="flex justify-between items-center mb-6">
        <form className="w-[50%] pr-4">
          <div className="relative">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="absolute top-0 bottom-0 w-6 h-6 my-auto text-gray-400 left-3"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              />
            </svg>
            <input
              type="text"
              placeholder="Search"
              className="w-full py-3 pl-12 pr-4 text-gray-500 border rounded-md outline-none bg-gray-50 focus:bg-white focus:border-indigo-600"
            />
              </div>
          </form>
        <div className="flex w-[50%] space-x-2 items-center justify-end text-custom-white">
          {/* Filter buttons or dropdowns */}
          <select className="p-2  border bg-custom-black rounded-sm w-full">
          <option selected >Date</option>
            <option  value="">&#60; 3 Days</option>
            <option value="">&#60; 10 Days</option>
            <option value="">&#60; 20 Days</option>
          </select>
          <select className="p-2  border bg-custom-black rounded-sm w-full">
            <option selected >Location</option>
            <option value="">BC</option>
            <option value="">ON</option>
            <option value="">AB</option>
          </select>
          <select className="p-2 border bg-custom-black rounded-sm w-full">
          <option selected >Job Title</option>
            <option value="">Software Engineer</option>
            <option value="">Software Developer</option>
            <option value="">Data Engineer</option>
            <option value="">Machine Learning</option>
            <option value="">Data Analyst</option>
          </select>
        </div>
      </div>
      
      <div>
        
        <div className="cursor-pointer grid grid-cols-1 md:grid-cols-2 gap-4 text-custom-black border mb-6">
        <audio ref={audioRef} src="/Jobhub Click.mp3" preload="auto"></audio>
        {jobsToShow.map(job => (
          <Link onClick={(event) => playAudioThenNavigate(job.link, event)} href={job.link} key={job.id} className="block border-2 border-gray-300 rounded-lg p-4 hover:border-custom-orange transition w-full">
            <div className="grid grid-cols-5">
              <div className="col-span-1 text-center">
                <p className="font-bold text-xl text-custom-orange">{formatDate(job.date).split(" ")[1]}</p>
                <p className="font-bold text-xl text-custom-black">{formatDate(job.date).split(" ")[2]}</p>
              </div>
              <div className="col-span-4 pl-4">
                <h2 className="font-bold text-xl">{job.position}</h2>
                <p>{job.company}</p>
                <p>{job.location}</p>
              </div>
            </div>
          </Link>
          ))}
        </div>
        <div className="flex justify-center items-center mb-2">
        {visibleJobsCount < jobs.length && (
          <button onClick={loadMoreJobs} className="bg-custom-black hover:bg-custom-orange text-center text-white p-2 rounded my-2 justify-center mx-auto">
            Load More
          </button>
        )}
        </div>
      </div>
    </div>
  );
};

export default JobListings;
