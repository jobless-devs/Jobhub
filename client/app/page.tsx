'use client'

import Head from 'next/head';
import Image from 'next/image';
import axios from 'axios';
import React, {useState, useEffect} from 'react';
import JobListings from './pages/job-listings';
import AboutUs from './pages/about-us';

type Job = {
  id: number;
  date: string;
  position: string;
  company: string;
  location: string;
  link: string;
};

const HomePage = () => {
  const [showJobListings, setShowJobs] = useState(false); 
  const [showAboutUs, setShowAboutUs] = useState(false);
  const [jobs, setJobs] = useState<Job[]>([]);

  useEffect(() => {
    const fetchJobs = async () => {
      try {
        const response = await axios.get('https://9loe6yy9pk.execute-api.us-east-1.amazonaws.com/prod/jobs');
        if (response.status === 200 && response.data) {
          const responseBody = typeof response.data.body === 'string' ? JSON.parse(response.data.body) : response.data.body;
          if (Array.isArray(responseBody)) {
            const fetchedJobs = responseBody.map((job: any) => ({
              id: job.id,
              date: job.date_posted,
              position: job.title,
              company: job.company,
              location: job.location,
              link: job.job_url
            }));
            setJobs(fetchedJobs);
          }
        }
      } catch (error) {
        console.error('Error fetching jobs:', error);
      }
    };
    fetchJobs();
  }, []);

  return (
    <>
      <Head>
        <title>Job Hub</title>
        <meta name="description" content="Find your dream job with Job Hub" />
      </Head>
      <div>
      {showJobListings ? (
          <JobListings jobs={jobs} onBack={() => setShowJobs(false)} />
          ) : showAboutUs ? (
            <AboutUs onBack={() => setShowAboutUs(false)} />
          ) : (
      <div className="bg-wallpaper">
        {/* Landing Page */}
        <div className="md:container md:mx-auto w-full h-screen flex flex-col justify-center py-4">
          <nav className="flex justify-between items-center py-4">
            <div className="jobhub-logo">
              <Image src="/images/Jobhub Logo.png" alt="Job Hub" className="w-60" width="240" height="300"/> 
            </div>
            <div className="flex space-x-16">
              <a onClick={() => { setShowAboutUs(false); setShowJobs(true); }} className="hover:bg-custom-black text-white px-6 py-2 rounded-full ">Jobs</a>
              <a onClick={() => { setShowAboutUs(true); setShowJobs(false); }} className="hover:bg-custom-black text-white px-6 py-2 rounded-full ">About Us</a>
              <a href="#login" className="hover:bg-custom-black text-white px-6 py-2 rounded-full border">Log In</a>
            </div>
          </nav>
          <div className="flex flex-1 mt-[10%]"> {/* Using margin to solve for now */}
            <div className="w-1/2">
              <div className="relative w-full">
                <Image 
                src="/images/Jobhub Landing.svg"
                alt="Dream Companies"
                layout="responsive"
                width={685}
                height={204}
                />
              </div>
            </div>
          
            <div className="w-1/2 text-center space-y-6 px-12 animate-slideIn">
              <h1 className="text-4xl font-bold">Your Career Starts Here! &#5171;</h1>
              <p className="text-xl text-center">
                Unleash your potential with real-world experiences. Explore, learn, and grow with our
                diverse internship opportunities.
              </p>
              <div className="flex justify-center items-center space-x-6 ">
                <button className="bg-custom-black hover:bg-custom-orange text-white font-semibold py-2 px-4 rounded-full" onClick={() => { setShowAboutUs(false); setShowJobs(true); }}>
                  Find Job
                </button>
                <button className="bg-custom-gray hover:bg-custom-orange text-white font-semibold hover:text-white py-2 px-4 rounded-full" onClick={() => { setShowAboutUs(true); setShowJobs(false); }}>
                  Learn More
                </button>
              </div>
            </div>
          </div>
          {/* Dare to Dream Section */}
          <div className="flex justify-center items-center w-full"> {/* Using image for now, will use the actual logo and texts*/}
            <div className="relative w-full">
              <Image 
              src="/images/Dream Logo.svg"
              alt="Dream Companies"
              layout="responsive"
              width={1442}
              height={281}
              />
            </div>
          </div>
        </div>
      </div>
      )}
      </div>
    </>
  );
};

export default HomePage;
