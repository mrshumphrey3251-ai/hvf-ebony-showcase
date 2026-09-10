import 'package:flutter/material.dart';
import 'mission_panel.dart'; 
import 'telemetry_feed.dart'; // Integrating the digital twin feed

// INITIATING LAYER 2: SENTINEL ULTRA COMMAND DECK
// Air-gapped Tactical Interface [PUBLIC SPECIFICATION]

void main() {
  runApp(const SentinelUltraApp());
}

class SentinelUltraApp extends StatelessWidget {
  const SentinelUltraApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sentinel Ultra Command Deck',
      theme: ThemeData(
        brightness: Brightness.dark,
        primaryColor: Colors.tealAccent,
        scaffoldBackgroundColor: Colors.black87,
      ),
      home: const DashboardScreen(),
    );
  }
}

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({Key? key}) : super(key: key);

  @override
  _DashboardScreenState createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  final String _apiStatus = "[INTERNAL CONNECTION LOGIC REDACTED]";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('HUMPHREY VIRTUAL FARMS - COMMAND DECK'),
        backgroundColor: Colors.black,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Card(
                color: Colors.black45,
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Icon(Icons.security, size: 40, color: Colors.tealAccent),
                      const SizedBox(width: 20),
                      Text(
                        'SYSTEM STATUS: \',
                        style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, letterSpacing: 1.5),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 20),
              // Rendering the Digital Twin Telemetry
              const TelemetryFeedPanel(),
              const SizedBox(height: 20),
              // Rendering the active Mission Control Panel
              const MissionControlPanel(),
            ],
          ),
        ),
      ),
    );
  }
}
