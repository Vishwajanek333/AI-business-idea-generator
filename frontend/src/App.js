import React, { useState } from 'react';
import { Sparkles, LogOut, Home, Zap, BarChart3, Download, Heart, Mail, Github, Eye, EyeOff } from 'lucide-react';

// Professional Logo Component
const Logo = ({ size = 40 }) => (
  <svg width={size} height={size} viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="50" r="48" fill="#1e3a8a" opacity="0.1"/>
    <defs>
      <linearGradient id="logoGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style={{stopColor: '#2563eb', stopOpacity: 1}} />
        <stop offset="100%" style={{stopColor: '#1e40af', stopOpacity: 1}} />
      </linearGradient>
    </defs>
    <path d="M 50 15 C 60 15 68 23 68 33 C 68 40 63 46 58 48 L 58 60 C 58 62 56 64 54 64 L 46 64 C 44 64 42 62 42 60 L 42 48 C 37 46 32 40 32 33 C 32 23 40 15 50 15 Z" fill="url(#logoGradient)"/>
    <line x1="50" y1="25" x2="50" y2="35" stroke="#fbbf24" strokeWidth="2" strokeLinecap="round"/>
    <line x1="42" y1="32" x2="50" y2="40" stroke="#fbbf24" strokeWidth="2" strokeLinecap="round" opacity="0.7"/>
    <line x1="58" y1="32" x2="50" y2="40" stroke="#fbbf24" strokeWidth="2" strokeLinecap="round" opacity="0.7"/>
    <path d="M 46 64 Q 46 70 50 75 Q 54 70 54 64" stroke="#2563eb" strokeWidth="2" fill="none"/>
    <circle cx="45" cy="28" r="4" fill="white" opacity="0.4"/>
  </svg>
);

export default function App() {
  const [currentPage, setCurrentPage] = useState('login');
  const [token, setToken] = useState('');
  const [username, setUsername] = useState('');
  const [ideas, setIdeas] = useState([]);
  const [formData, setFormData] = useState({ keywords: '', industry: '', num_ideas: 1 });
  const [loading, setLoading] = useState(false);
  const [loginData, setLoginData] = useState({ username: '', password: '' });
  const [showPassword, setShowPassword] = useState(false);
  const [favorites, setFavorites] = useState([]);
  const [loginError, setLoginError] = useState('');

  const API_URL = 'http://localhost:8000/api/v1';

  const handleLogin = async () => {
    setLoginError('');
    if (!loginData.username || !loginData.password) {
      setLoginError('Please enter username and password');
      return;
    }
    try {
      const url = `${API_URL}/auth/login?username=${encodeURIComponent(loginData.username)}&password=${encodeURIComponent(loginData.password)}`;
      
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      
      const data = await response.json();
      
      if (data.access_token) {
        setToken(data.access_token);
        setUsername(loginData.username);
        setCurrentPage('dashboard');
        setLoginData({ username: '', password: '' });
      } else {
        setLoginError(data.detail || 'Login failed');
      }
    } catch (error) {
      setLoginError('Connection error: ' + error.message);
    }
  };
const handleGenerateIdeas = async () => {
  if (!formData.keywords || !formData.industry) {
    alert('Please fill in all fields');
    return;
  }
  setLoading(true);
  try {
    console.log('Generating ideas with:', formData);
    const response = await fetch(`${API_URL}/ideas/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(formData)
    });
    
    console.log('Response status:', response.status);
    
    if (!response.ok) {
      const errorData = await response.json();
      console.error('Error:', errorData);
      alert('Error: ' + (errorData.detail || 'Failed to generate ideas'));
      setLoading(false);
      return;
    }
    
    const data = await response.json();
    console.log('Ideas received:', data);
    setIdeas(Array.isArray(data) ? data : []);
  } catch (error) {
    console.error('Generation error:', error);
    alert('Error generating ideas: ' + error.message);
  } finally {
    setLoading(false);
  }
};
 

  const toggleFavorite = (idx) => {
    if (favorites.includes(idx)) {
      setFavorites(favorites.filter(i => i !== idx));
    } else {
      setFavorites([...favorites, idx]);
    }
  };

  const handleLogout = () => {
    setToken('');
    setUsername('');
    setIdeas([]);
    setFavorites([]);
    setCurrentPage('login');
  };

  // Login Page
  if (currentPage === 'login') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-600 via-blue-500 to-indigo-700 flex items-center justify-center p-4 relative overflow-hidden">
        <div className="absolute top-10 right-10 w-40 h-40 bg-white opacity-5 rounded-full blur-3xl"></div>
        <div className="absolute bottom-10 left-10 w-40 h-40 bg-white opacity-5 rounded-full blur-3xl"></div>

        <div className="w-full max-w-md relative z-10">
          <div className="bg-white rounded-3xl shadow-2xl p-8 backdrop-blur-sm">
            <div className="flex justify-center mb-8">
              <Logo size={60} />
            </div>
            <h1 className="text-3xl font-bold text-center text-gray-800 mb-2">AI Idea Generator</h1>
            <p className="text-center text-gray-600 mb-8 text-sm">Transform your ideas into viable business plans powered by AI</p>

            <div className="space-y-4 mb-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Username</label>
                <input
                  type="text"
                  placeholder="eg. Ram"
                  value={loginData.username}
                  onChange={(e) => setLoginData({...loginData, username: e.target.value})}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600 transition"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Password</label>
                <div className="relative">
                  <input
                    type={showPassword ? "text" : "password"}
                    placeholder="Enter your password"
                    value={loginData.password}
                    onChange={(e) => setLoginData({...loginData, password: e.target.value})}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600 transition"
                  />
                  <button
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-3 text-gray-600"
                  >
                    {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
                  </button>
                </div>
              </div>

              {loginError && (
                <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-2 rounded-lg text-sm">
                  {loginError}
                </div>
              )}

              <button
                onClick={handleLogin}
                className="w-full bg-gradient-to-r from-blue-600 to-blue-700 text-white py-3 rounded-lg font-semibold hover:shadow-lg transition transform hover:scale-105"
              >
                Sign In
              </button>
            </div>

            <div className="flex items-center gap-4 my-6">
              <div className="flex-1 h-px bg-gray-300"></div>
              <span className="text-gray-500 text-sm">or</span>
              <div className="flex-1 h-px bg-gray-300"></div>
            </div>

            <div className="grid grid-cols-2 gap-4 mb-6">
              <button onClick={() => alert('Gmail login coming soon!')} className="flex items-center justify-center gap-2 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition">
                <Mail size={18} className="text-red-600" />
                <span className="text-sm font-medium text-gray-700">Gmail</span>
              </button>
              <button onClick={() => alert('GitHub login coming soon!')} className="flex items-center justify-center gap-2 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition">
                <Github size={18} className="text-gray-800" />
                <span className="text-sm font-medium text-gray-700">GitHub</span>
              </button>
            </div>
          </div>

          <p className="text-center text-white text-xs mt-6">By signing in, you agree to our Terms of Service</p>
        </div>
      </div>
    );
  }

  // Main Dashboard
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-3">
            <Logo size={40} />
            <div>
              <h1 className="text-xl font-bold text-gray-800">AI Idea Generator</h1>
              <p className="text-xs text-gray-600">Finance • Education • Social</p>
            </div>
          </div>

          <div className="hidden md:flex gap-2">
            <button
              onClick={() => setCurrentPage('dashboard')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition ${currentPage === 'dashboard' ? 'bg-blue-100 text-blue-700' : 'text-gray-600 hover:bg-gray-100'}`}
            >
              <Home className="w-5 h-5" /> Dashboard
            </button>
            <button
              onClick={() => setCurrentPage('generate')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition ${currentPage === 'generate' ? 'bg-blue-100 text-blue-700' : 'text-gray-600 hover:bg-gray-100'}`}
            >
              <Zap className="w-5 h-5" /> Generate
            </button>
            <button
              onClick={() => setCurrentPage('analytics')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition ${currentPage === 'analytics' ? 'bg-blue-100 text-blue-700' : 'text-gray-600 hover:bg-gray-100'}`}
            >
              <BarChart3 className="w-5 h-5" /> Analytics
            </button>
          </div>

          <div className="flex items-center gap-4">
            <div className="hidden sm:block text-right">
              <p className="text-sm font-medium text-gray-800">{username}</p>
              <p className="text-xs text-gray-500">Active User</p>
            </div>
            <button
              onClick={handleLogout}
              className="flex items-center gap-2 px-4 py-2 text-red-600 hover:bg-red-50 rounded-lg font-medium transition"
            >
              <LogOut className="w-5 h-5" /> Logout
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8">
        {currentPage === 'dashboard' && (
          <div className="space-y-8">
            <div className="bg-gradient-to-r from-blue-600 via-blue-700 to-indigo-800 text-white rounded-2xl p-8 shadow-lg">
              <h2 className="text-4xl font-bold mb-2">Welcome back, {username}! 👋</h2>
              <p className="text-blue-100 text-lg">Generate innovative business ideas in Finance, Education, and Social sectors</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
              <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-gray-600 text-sm mb-1">Total Ideas</p>
                    <p className="text-3xl font-bold text-gray-800">{ideas.length}</p>
                  </div>
                  <div className="bg-blue-100 p-3 rounded-lg">
                    <Sparkles className="w-6 h-6 text-blue-600" />
                  </div>
                </div>
              </div>

              <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-gray-600 text-sm mb-1">Favorites</p>
                    <p className="text-3xl font-bold text-gray-800">{favorites.length}</p>
                  </div>
                  <div className="bg-red-100 p-3 rounded-lg">
                    <Heart className="w-6 h-6 text-red-600" />
                  </div>
                </div>
              </div>

              <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-gray-600 text-sm mb-1">Finance Ideas</p>
                    <p className="text-3xl font-bold text-gray-800">{ideas.filter(i => i.industry === 'FinTech').length}</p>
                  </div>
                  <div className="bg-green-100 p-3 rounded-lg">
                    <BarChart3 className="w-6 h-6 text-green-600" />
                  </div>
                </div>
              </div>

              <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-gray-600 text-sm mb-1">Quick Start</p>
                    <p className="text-sm font-medium text-blue-600 mt-2">Generate Now</p>
                  </div>
                  <div className="bg-purple-100 p-3 rounded-lg">
                    <Zap className="w-6 h-6 text-purple-600" />
                  </div>
                </div>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl border-2 border-blue-200 p-6 cursor-pointer hover:shadow-lg transition" onClick={() => setCurrentPage('generate')}>
                <h3 className="text-lg font-semibold text-blue-900 mb-2">Finance Ideas</h3>
                <p className="text-blue-800 text-sm mb-4">Generate FinTech and investment ideas</p>
                <button className="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-blue-700">
                  Create Now
                </button>
              </div>

              <div className="bg-gradient-to-br from-green-50 to-green-100 rounded-xl border-2 border-green-200 p-6 cursor-pointer hover:shadow-lg transition" onClick={() => setCurrentPage('generate')}>
                <h3 className="text-lg font-semibold text-green-900 mb-2">Education Ideas</h3>
                <p className="text-green-800 text-sm mb-4">Create EdTech and learning platform ideas</p>
                <button className="bg-green-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-green-700">
                  Create Now
                </button>
              </div>

              <div className="bg-gradient-to-br from-purple-50 to-purple-100 rounded-xl border-2 border-purple-200 p-6 cursor-pointer hover:shadow-lg transition" onClick={() => setCurrentPage('generate')}>
                <h3 className="text-lg font-semibold text-purple-900 mb-2">Social Ideas</h3>
                <p className="text-purple-800 text-sm mb-4">Generate social impact and community ideas</p>
                <button className="bg-purple-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-purple-700">
                  Create Now
                </button>
              </div>
            </div>
          </div>
        )}

        {currentPage === 'generate' && (
          <div className="space-y-8">
            <div>
              <h2 className="text-3xl font-bold text-gray-800 mb-2">Generate Business Ideas</h2>
              <p className="text-gray-600">Create innovative ideas for Finance, Education, and Social sectors</p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
              <div className="lg:col-span-1">
                <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 sticky top-24">
                  <h3 className="text-xl font-semibold text-gray-800 mb-6">Idea Parameters</h3>
                  <div className="space-y-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">Keywords</label>
                      <input
                        type="text"
                        placeholder="e.g., AI + Education"
                        value={formData.keywords}
                        onChange={(e) => setFormData({...formData, keywords: e.target.value})}
                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                      />
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">Industry Sector</label>
                      <select
                        value={formData.industry}
                        onChange={(e) => setFormData({...formData, industry: e.target.value})}
                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                      >
                        <option value="">Select Sector</option>
                        <option value="FinTech">Finance (FinTech)</option>
                        <option value="EdTech">Education (EdTech)</option>
                        <option value="Social">Social Impact</option>
                        <option value="E-commerce">E-commerce</option>
                        <option value="SaaS">SaaS</option>
                      </select>
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">Number of Ideas</label>
                      <input
                        type="number"
                        min="1"
                        max="5"
                        value={formData.num_ideas}
                        onChange={(e) => setFormData({...formData, num_ideas: parseInt(e.target.value)})}
                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                      />
                    </div>

                    <button
                      onClick={handleGenerateIdeas}
                      disabled={loading}
                      className="w-full bg-gradient-to-r from-blue-600 to-blue-700 text-white py-3 rounded-lg font-semibold hover:shadow-lg transition disabled:opacity-50"
                    >
                      {loading ? 'Generating...' : 'Generate Ideas'}
                    </button>
                  </div>
                </div>
              </div>

              <div className="lg:col-span-2">
                {ideas.length > 0 ? (
                  <div className="space-y-4">
                    {ideas.map((idea, idx) => (
                      <div key={idx} className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-lg transition">
                        <div className="flex justify-between items-start mb-4">
                          <div className="flex-1">
                            <h3 className="text-xl font-semibold text-gray-800">{idea.title}</h3>
                            <span className="inline-block mt-2 px-3 py-1 bg-blue-100 text-blue-700 text-xs font-medium rounded-full">{idea.industry}</span>
                          </div>
                          <div className="flex gap-2">
                            <button
                              onClick={() => toggleFavorite(idx)}
                              className={`p-2 rounded-lg transition ${favorites.includes(idx) ? 'text-red-600 bg-red-50' : 'text-gray-500 hover:bg-gray-100'}`}
                            >
                              <Heart className="w-5 h-5" fill={favorites.includes(idx) ? 'currentColor' : 'none'} />
                            </button>
                            <button className="p-2 text-gray-500 hover:bg-gray-100 rounded-lg">
                              <Download className="w-5 h-5" />
                            </button>
                          </div>
                        </div>

                        <p className="text-gray-700 mb-4">{idea.description}</p>

                        <div className="grid grid-cols-2 gap-4 text-sm">
                          <div className="bg-gray-50 p-3 rounded-lg">
                            <p className="font-semibold text-gray-700 mb-1">Business Model</p>
                            <p className="text-gray-600 text-xs">{idea.business_model}</p>
                          </div>
                          <div className="bg-gray-50 p-3 rounded-lg">
                            <p className="font-semibold text-gray-700 mb-1">Target Audience</p>
                            <p className="text-gray-600 text-xs">{idea.target_audience}</p>
                          </div>
                          <div className="bg-gray-50 p-3 rounded-lg col-span-2">
                            <p className="font-semibold text-gray-700 mb-1">Market Potential</p>
                            <p className="text-gray-600 text-xs">{idea.market_potential}</p>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                ) : (
                  <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-12 text-center">
                    <Zap className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                    <p className="text-gray-600 text-lg">Fill in the parameters and generate your first business idea</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {currentPage === 'analytics' && (
          <div className="space-y-8">
            <div>
              <h2 className="text-3xl font-bold text-gray-800 mb-2">Analytics & Insights</h2>
              <p className="text-gray-600">Track your idea generation activity and trends</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
                <p className="text-gray-600 text-sm mb-2">Total Ideas</p>
                <p className="text-3xl font-bold text-blue-600">{ideas.length}</p>
              </div>
              <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
                <p className="text-gray-600 text-sm mb-2">Favorite Ideas</p>
                <p className="text-3xl font-bold text-red-600">{favorites.length}</p>
              </div>
              <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
                <p className="text-gray-600 text-sm mb-2">Finance Ideas</p>
                <p className="text-3xl font-bold text-green-600">{ideas.filter(i => i.industry === 'FinTech').length}</p>
              </div>
              <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
                <p className="text-gray-600 text-sm mb-2">Education Ideas</p>
                <p className="text-3xl font-bold text-purple-600">{ideas.filter(i => i.industry === 'EdTech').length}</p>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}