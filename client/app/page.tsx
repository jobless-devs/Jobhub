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
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

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

      // Wallpaper for the Whole Screen
      <div className="bg-wallpaper flex flex-col min-h-screen overflow-hidden">

        {/* Landing Page Navigation Bar and Logo*/}
        <div className="pt-4 mx-auto mx-auto w-full flex flex-col justify-center py-4">
          <nav className="flex justify-between items-center px-4 md:px-8 relative">
            <div className="jobhub-logo  ">
              <Image src="/images/Jobhub Logo.png" alt="Job Hub" className="md:w-60" width="150" height="300"/> 
            </div>
            <button onClick={toggleMobileMenu} className="md:hidden">
              <span className='text-3xl'>&#9776;</span> {/* Replace with an icon */}
            </button>
            <div className={`${isMobileMenuOpen ? 'flex' : 'hidden'} flex-col absolute top-full right-0 bg-white shadow-md py-2 w-full z-50`}>
              <a onClick={() => { setShowAboutUs(false); setShowJobs(true); toggleMobileMenu();}} className="hover:bg-custom-black text-custom-black px-6 py-2 rounded-full ">Jobs</a>
              <a onClick={() => { setShowAboutUs(true); setShowJobs(false); toggleMobileMenu();}} className="hover:bg-custom-black text-custom-black px-6 py-2 rounded-full ">About Us</a>
              <a href="#login" className="hover:bg-custom-black text-custom-black px-6 py-2 rounded-full border">Log In</a>
            </div>
            <div className="hidden md:flex space-x-16 text-center items-center">
              <a onClick={() => { setShowAboutUs(false); setShowJobs(true); }}  className="text-white hover:bg-custom-black text-custom-black px-6 py-2 rounded-full">Jobs</a>
              <a onClick={() => { setShowAboutUs(false); setShowJobs(true); }}  className="text-white hover:bg-custom-black text-custom-black px-6 py-2 rounded-full">About Us</a>
              <a href="#login" className="text-white hover:bg-custom-black text-white px-6 py-2 rounded-full border">Log In</a>
            </div>
          </nav>
        </div>

        {/* Landing Page Content */}
        <div className=" md:mx-auto w-full flex flex-col md:flex-row justify-center items-center py-4 px-4 md:px-8 mt-[10%]">
          <div className="md:w-1/2 flex justify-center mb-8">
            <div className="relative w-full max-w-md">
              <Image 
                src="/images/Jobhub Landing.svg"
                alt="Dream Companies"
                layout="responsive"
                width={685}
                height={204}
              />
            </div>
          </div>

          <div className="md:w-1/2 md:space-y-4 mb-[20%] md:mb-0 flex flex-col text-center space-y-6 px-12 animate-slideIn">
            <h1 className="md:text-4xl text-2xl font-bold">Your Career Starts Here! &#5171;</h1>
            <p className="md:text-xl text-md text-center">
              Unleash your potential with real-world experiences. Explore, learn, and grow with our
              diverse internship opportunities.
            </p>
            <div className="flex justify-center items-center space-x-6 ">
              <button className="bg-custom-black hover:bg-custom-orange text-white font-semibold py-2 px-4 rounded-full " onClick={() => { setShowAboutUs(false); setShowJobs(true); }}>
                Find Job
              </button>
              <button className="bg-custom-gray hover:bg-custom-orange text-white font-semibold hover:text-white py-2 px-4 rounded-full" onClick={() => { setShowAboutUs(true); setShowJobs(false); }}>
                Learn More
              </button>
            </div>
          </div>
        </div>
          
          {/* Dare to Dream Section */}
          <div className='bottom-0 md:absolute relative w-full'>
            <div className="flex flex-grow w-full "> {/* Using image for now, will use the actual logo and texts*/}
              <div className="relative w-full block md:hidden">
                <Image 
                  src="/images/Dream Logo-Mobile.svg" // Replace with your mobile image
                  alt="Dream Companies Mobile"
                  layout="responsive"
                  width={560} // Adjust based on your mobile image's aspect ratio
                  height={536}
                />
              </div>
              <div className="relative w-full hidden md:block">
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
