package agventure.com.Krish_e;

import android.content.Intent;
import android.net.Uri;;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button diseaseDetectionBt = findViewById(R.id.disease_detection_button);
        Button GovPortalBt = findViewById(R.id.Gov_portal_button);
        Button TechnologyUpdatesBt = findViewById(R.id.Technology_updates_button);

        diseaseDetectionBt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), KrishiActivity.class);
                startActivity(intent);
            }
        });

        GovPortalBt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Uri uri = Uri.parse("https://farmer.gov.in/");

                Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                startActivity(intent);
            }
        });

        TechnologyUpdatesBt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Uri uri = Uri.parse("http://www.realagriculture.com/");

                Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                startActivity(intent);
            }
        });

    }
}




